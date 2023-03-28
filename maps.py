#------------------------------------------------------------------------------
# Author: Yunus Emre Işıkdemir
# 
# Create Date: 02/11/2021
#
# Project Name: Point Cloud Data Visualizer Graphical User Interface
#
# Description: The script presented herein offers a visualization tool capable 
#              of representing semantic, topological, and metric maps.
# 
#------------------------------------------------------------------------------

import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from configs import Configure
from layout import Window

class SARSTM:
    def __init__(self) -> None:
        self.map_config = Configure()
        self.map_config.read_file()
        self.map_handler = Window()
        self.map_handler.button_point_cloud.clicked.connect(self.plot_all_maps)
        self.map_handler.next_cloud.clicked.connect(self.map_config.get_next_scene)
        self.map_handler.reset_button.clicked.connect(self.map_config.reset_path)
        self.map_handler.horizontalSlider.valueChanged.connect(self.map_config.set_point_size)
        self.map_handler.horizontalSlider2.valueChanged.connect(self.map_config.set_alpha)

    def change_dir(self, new_path: str) -> None:
        self.pcd_path = new_path

    def plot_all_maps(self) -> None:
        self.__plot_metric()
        self.__plot_semantic()
        self.__plot_point_cloud()
        self.__plot_topologic()

    def __plot_metric(self) -> None:
        occupied = pd.read_csv(self.map_config.occupied_path, 
                               sep=" ", 
                               header=None).drop(3, axis=1)
        occupied.columns = ["x", "y", "z"]

        empty = pd.read_csv(self.map_config.empty_path, 
                            sep=" ", 
                            header=None).drop(3, axis=1)
        empty.columns = ["x", "y", "z"]

        self.ax1 = self.map_handler.figure.add_subplot(221, projection="3d")
        self.ax1.scatter(
            occupied.x,
            occupied.y,
            occupied.z,
            color="red",
            s=self.map_config.point_size * 10,
            marker="s",
            alpha=self.map_config.alpha_param / 2,
        )

        self.ax1.scatter(
            empty.x,
            empty.y,
            empty.z,
            color="green",
            s=self.map_config.point_size * 10,
            marker="s",
            alpha=self.map_config.alpha_param / 4,
        )

        self.ax1.title.set_text("Metric Map")
        plt.axis("off")
        self.ax1.set_facecolor("dimgray")
        self.map_handler.canvas.draw()

    def __plot_semantic(self) -> None:
        semantic = pd.read_csv(self.map_config.semantic_path, 
                               sep=",", 
                               usecols=["x", "y", "z", "label"])

        self.ax2 = self.map_handler.figure.add_subplot(222, projection="3d")
        planes = ["wall", "inclined", "terrain", "straight"]
        colors = ["red", "blue", "yellow", "purple"]
        for plane, color in zip(planes, colors):
            plane_type = semantic[semantic.label == plane]
            self.ax2.scatter(
                plane_type.x,
                plane_type.y,
                plane_type.z,
                color=color,
                s=self.map_config.point_size,
                alpha=self.map_config.alpha_param,
            )

        self.ax2.title.set_text("Semantic Map")
        plt.axis("off")
        self.ax2.set_facecolor("dimgray")
        self.map_handler.canvas.draw()

    def __plot_point_cloud(self) -> None:
        point_cloud = pd.read_csv(self.map_config.occupied_path, 
                                  sep=" ", 
                                  header=None).drop(3, axis=1)
        point_cloud.columns = ["x", "y", "z"]

        self.ax3 = self.map_handler.figure.add_subplot(223, projection="3d")
        self.ax3.scatter(
            point_cloud.x,
            point_cloud.y,
            point_cloud.z,
            color="lightblue",
            s=self.map_config.point_size,
            alpha=self.map_config.alpha_param,
        )

        self.ax3.title.set_text("Point Cloud")
        plt.axis("off")
        self.ax3.set_facecolor("dimgray")
        self.map_handler.canvas.draw()

    def __plot_topologic(self) -> None:
        node = pd.read_csv(self.map_config.topological_path, 
                           sep=" ", 
                           header=None).drop(3, axis=1)
        node.columns = ["x", "y", "z"]

        occupied = pd.read_csv(self.map_config.occupied_path, 
                               sep=" ", 
                               header=None).drop(3, axis=1)
        occupied.columns = ["x", "y", "z"]


        self.ax4 = self.map_handler.figure.add_subplot(224, projection="3d")
        self.ax4.scatter(
            occupied.x,
            occupied.y,
            occupied.z,
            color="lightblue",
            s=self.map_config.point_size,
            alpha=self.map_config.alpha_param / 2,
        )

        self.ax4.scatter(
            node.x,
            node.y,
            node.z,
            color="orange",
            s=self.map_config.point_size * 15,
            alpha=self.map_config.alpha_param,
        )

        self.ax4.title.set_text("Topological Map")
        plt.axis("off")
        self.ax4.set_facecolor("dimgray")
        self.map_handler.canvas.draw()
