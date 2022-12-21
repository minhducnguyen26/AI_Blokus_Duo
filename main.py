# Everything you need to know about Blokus Duo:
# https://service.mattel.com/instruction_sheets/FWG43-Eng.pdf 

from blokus_duo import BlokusDuo
from player import Player

def main():
    env = BlokusDuo()

    # Player 1
    agent_1_id = 1
    agent_1 = Player(agent_1_id, env.board)

    # Player 2
    agent_2_id = 2
    agent_2 = Player(agent_2_id, env.board)

    while not agent_1.done() or not agent_2.done():
        # Player 1
        agent_1_made_valid_move = False

        # Allow the agent to think about making a move
        # until it actually makes a valid move
        while not agent_1_made_valid_move:    
            percepts = env.get_observable_percepts()

            agent_1.update_from_percepts(percepts)

            column_1, row_1, piece_shape_1 = agent_1.make_a_move(use_minimax=True)

            agent_1_made_valid_move = env.apply_actions(column_1, row_1, piece_shape_1, agent_1_id)

            if agent_1_made_valid_move:
                agent_1.made_valid_move(piece_shape_1)

        # Player 2
        agent_2_made_valid_move = False
        while not agent_2_made_valid_move:
            percepts = env.get_observable_percepts()

            agent_2.update_from_percepts(percepts)

            column_2, row_2, piece_shape_2 = agent_2.make_a_move()
            
            agent_2_made_valid_move = env.apply_actions(column_2, row_2, piece_shape_2, agent_2_id)

            if agent_2_made_valid_move:
                agent_2.made_valid_move(piece_shape_2)

    agent_1_score = agent_1.get_score()
    agent_2_score = agent_2.get_score()

    env.evaluate_game_result(agent_1_score, agent_2_score)

if __name__ == "__main__":
    main()
    print()