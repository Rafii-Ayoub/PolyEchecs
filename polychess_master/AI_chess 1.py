# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 14:20:34 2020

@author: Admin
"""

class State:
  def total_eval(self, player_color):
        """
            Evaluation Function
            The formula is:
            0.5(total_player_pawn_hp - total_enemy_pawn_hp) +
            0.1(total_player_pawn_atk - total_enemy_pawn_atk) +
            0.1(total_player_pawn_step - total_enemy_pawn_step) +
            5(total_enemy_dead_pawn - total_player_dead_pawn) +
            1(player_king_hp - enemy_king_hp)
            Parameters
            ----------
            player_color : the player_index

            Returns
            -------
            int
                how far is the advantage of a player
        """
        (player_king, enemy_king) = (self.white_king, self.black_king) if player_color == 0 else (self.black_king, self.white_king)
        (current_player_pawn_list, enemy_pawn_list) = (self.white_pawn_list, self.black_pawn_list) if player_color == 0 else (self.black_pawn_list, self.white_pawn_list)
        
        ## UTILITY
        if self.is_terminal():
            if player_king.dead:
                return -120
            elif enemy_king.dead:
                return 120
            else:
                util_value = 0
                for player_pawn, enemy_pawn in zip(current_player_pawn_list,enemy_pawn_list):
                    util_value += (int(enemy_pawn.dead) - int(player_pawn.dead))
                if util_value < 0:
                    util_value = -120
                else:
                    util_value = 120
                return util_value
        
        ## EVALUATION OR HEURISTIC
        eval_value = 0
        for player_pawn, enemy_pawn in zip(current_player_pawn_list,enemy_pawn_list):

            if not player_pawn.dead:
                eval_value += 0.3 * player_pawn.hp
            if not enemy_pawn.dead:
                eval_value -= 0.3 * enemy_pawn.hp
            if player_pawn.status and not player_pawn.dead:
                eval_value += 0.1 * player_pawn.atk + 0.1 * player_pawn.step
            if enemy_pawn.status and not enemy_pawn.dead:
                eval_value -= 0.1 * enemy_pawn.atk - 0.1 * enemy_pawn.step
            eval_value += (int(enemy_pawn.dead) - int(player_pawn.dead)) * 10

        eval_value += player_king.hp - enemy_king.hp

        return eval_value
    
from test_helpers import heuristic_gen, get_successors
from node import Node





class AI():
    def __init__(self, max_depth=4, branches=2, leaf_nodes=[]):
        self.branches = branches
        self.max_depth = max_depth
        self.leaf_nodes = heuristic_gen(leaf_nodes)

    def get_moves(self):
        return get_successors(self.branches)

    def get_heuristic(self, board_state):
        return next(self.leaf_nodes)

    def minimax(self, node, current_depth=0):
        current_depth += 1
        if current_depth == self.max_depth:
            # get heuristic of each node
            node.value = self.get_heuristic(node.board_state)
            return node.value
        if current_depth % 2 == 0:
            # min player's turn
            return min([self.minimax(child_node, current_depth) for child_node in self.get_moves()])
        else:
            # max player's turn
            return max([self.minimax(child_node, current_depth) for child_node in self.get_moves()])

if __name__ == "__main__":
    import unittest
    class Test_minimax(unittest.TestCase):
        def test_minimax(self):
            data_set_1 = [8, 12, -13, 4, 1, 1, 20, 17, -5,
                          -1, -15, -12, -11, -1, 1, 17, -3, 12,
                          -7, 14, 9, 18, 4, -15, 8, 0, -6]
            first_test_AI = AI(4, 3, data_set_1)
            self.assertEqual(first_test_AI.minimax(Node()), 8, "Should return 8")
            data_set_2 = [-4, -17, 6, 10, -6, -1, 16, 12, -12,
                          16, -18, -18, -20, -15, -18, -8, 8, 0,
                          11, -14, 11, -20, 8, -2, -17, -18,
                          -11, 10, -8, -14, 7, -17]
            second_test_AI = AI(6, 2, data_set_2)
            self.assertEqual(second_test_AI.minimax(Node()), -8, "Should return -8")
    unittest.main()