import unittest

from maze import Maze


class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
                len(m1._cells),
                num_cols,
        )
        self.assertEqual(
                len(m1._cells[0]),
                num_rows,
        )
        self.assertEqual(
                m1._cells[0][0].has_top_wall,
                False,
        )
        self.assertEqual(
                m1._cells[-1][-1].has_bottom_wall,
                False,
        )

        visiteds = []
        for col in m1._cells:
            for cell in col:
                visiteds.append(cell.visited)
        self.assertFalse(any(visiteds))


    def test_maze_create_cells_large(self):
        num_cols = 50
        num_rows = 40
        m2 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
                len(m2._cells),
                num_cols,
        )
        self.assertEqual(
                len(m2._cells[0]),
                num_rows,
        )
        self.assertEqual(
                m2._cells[0][0].has_top_wall,
                False,
        )
        self.assertEqual(
                m2._cells[-1][-1].has_bottom_wall,
                False,
        )

        visiteds = []
        for col in m2._cells:
            for cell in col:
                visiteds.append(cell.visited)
        self.assertFalse(any(visiteds))



if __name__ == "__main__":
    unittest.main()
