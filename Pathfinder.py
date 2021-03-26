from Physics import Physics
from GameData import GameData
import math

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]


class Pathfinder:
    table = []

    @staticmethod
    def reset_table():
        Pathfinder.table = []
        for i in range(GameData.current_level.rows):
            row = []
            for j in range(GameData.current_level.cols):
                row.append(0)
            Pathfinder.table.append(row)

    @staticmethod
    def update_table():
        Pathfinder.reset_table()

        for solid in Physics.solids:
            solid_world_x, solid_world_y = solid.position.x // GameData.tile_size, solid.position.y // GameData.tile_size
            Pathfinder.table[solid_world_y][solid_world_x] = math.inf

        Pathfinder.bfs()
        # print(*Pathfinder.table, sep="\n")

    @staticmethod
    def in_bounds(world_row, world_col):
        if 0 <= world_col < len(Pathfinder.table[0]) and 0 <= world_row < len(Pathfinder.table):
            return True
        return False

    @staticmethod
    def bfs():
        player_world_x, player_world_y = GameData.player.position.x // GameData.tile_size, GameData.player.position.y // GameData.tile_size
        # Pathfinder.table[player_world_y][player_world_x] = 'p'
        q = [(player_world_y, player_world_x)]
        visited = [(player_world_y, player_world_x)]

        while len(q):
            for dir in directions:
                # check if it is in bounds
                if Pathfinder.in_bounds(q[0][0] + dir[0], q[0][1] + dir[1]):
                    if Pathfinder.table[q[0][0] + dir[0]][q[0][1] + dir[1]] == 0 and (q[0][0] + dir[0],
                                                                                      q[0][1] + dir[1]) not in visited:
                        Pathfinder.table[q[0][0] + dir[0]][q[0][1] + dir[1]] = Pathfinder.table[q[0][0]][q[0][1]] + 1
                        q.append((q[0][0] + dir[0], q[0][1] + dir[1]))
                        visited.append((q[0][0] + dir[0], q[0][1] + dir[1]))
            q.pop(0)

        # print(*Pathfinder.table, sep="\n")

    @staticmethod
    def get_smaller_cell_dir(position):
        world_col, world_row = position.x // GameData.tile_size, position.y // GameData.tile_size

        for dir in directions:
            if Pathfinder.in_bounds(world_row + dir[1], world_col + dir[0]):
                if Pathfinder.table[world_row + dir[1]][world_col + dir[0]] <= Pathfinder.table[world_row][
                    world_col] - 1:
                    return dir
        return None

    @staticmethod
    def get_cell_value(position):
        world_col, world_row = position.x // GameData.tile_size, position.y // GameData.tile_size

        if Pathfinder.in_bounds(world_row, world_col):
            return Pathfinder.table[world_row][world_col]
        return 0;
