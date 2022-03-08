import json


class FileHandler:

    def __init__(self):
        self.directory = "data/grid.json"

    def export_grid(self, grid):

        grid_dict = {
            "nodes": []
        }

        for row in range(len(grid)):

            for column in range(len(grid[row])):

                temp_dict = {
                    "pos": [],
                    "type": ""
                }

                if grid[row][column].is_start():
                    temp_dict["type"] = "start"
                elif grid[row][column].is_end():
                    temp_dict["type"] = "end"
                elif grid[row][column].is_barrier():
                    temp_dict["type"] = "room"
                else:
                    temp_dict["type"] = "empty"
                temp_dict["pos"] = [row, column]

                grid_dict["nodes"].append(temp_dict)

        try:
            with open(self.directory, "w") as file:
                json.dump(grid_dict, file)
        except FileNotFoundError:
            raise FileNotFoundError
