#------------------------------------------------------------------------------
# Author: Yunus Emre Işıkdemir
# 
# Create Date: 02/11/2021
#
# Project Name: Point Cloud Data Visualizer Graphical User Interface
#
# Description: The script provides the ability to customize visual settings to 
#              suit individual preferences.
# 
#------------------------------------------------------------------------------

from typing import List, Tuple
import os

class Configure:
    def __init__(self, point_size: int = 5, alpha_value: float = 0.9) -> None:
        self.point_size = point_size
        self.alpha_param = alpha_value
        self.pcd_path = ""
        self.occupied_path = ""
        self.empty_path = ""
        self.topological_path = ""
        self.semantic_path = ""
        self.file_indexer = 0
        self.read_file()

    def read_file(self) -> None:
        map_types: List[str] = ["occupied", "empty", "topological", "semantic"]
        map_paths: List[str] = []
        for types in map_types:
            prefix: str = os.path.join("scenes", f"sahne{self.file_indexer}")
            postfix: str = f"{self.file_indexer}_{types}.csv"
            map_paths.append(os.path.join(prefix, postfix))
        (
            self.occupied_path,
            self.empty_path,
            self.topological_path,
            self.semantic_path,
        ) = map_paths

    def get_next_scene(self) -> None:
        if self.file_indexer < 5:
            self.file_indexer += 1
        self.read_file()

    def reset_path(self) -> None:
        self.file_indexer = 0
        self.read_file()

    def get_point_size(self) -> int:
        return self.point_size

    def get_alpha(self) -> float:
        return self.alpha_param
    
    def set_point_size(self, point_size: int) -> None:
        self.point_size = point_size
        print("Point Size set to ", self.point_size)

    def set_alpha(self, alpha_param: float) -> None:
        self.alpa_param = alpha_param / 10
        print("Alpha set to ", self.alpa_param)
