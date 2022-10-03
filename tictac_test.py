3
�:;c�  �               @   s:   d dl mZ d dlZd dlZG dd� dej�Zej�  dS )�    )�	TicTacToeNc               @   sL   e Zd Zdd� Zdd� Zdd� Zdd� Zd	d
� Zdd� Zdd� Z	dd� Z
dS )�TestTicTacToec             C   s   t � }| j|jjd� d S )N�   )r   r   )r   �assertEqualZboard�shape)�self�ttt� r	   �tictac_test.py�test_init_board   s    zTestTicTacToe.test_init_boardc             C   s�   t jd�}d|d< d	|d
< d|d< d}|j� }d|d< d}t||�}|j� \}}tdj|�� tdj|�� | j||� | j|j� |j� � d S )Nr   �   r   �   z
final board = 
{}zexpected board = 
{})r   r   )r   r   �����)r   r   )r   r   )r   r   )	�npZzeros�copyr   �	play_game�print�formatr   �tolist)r   �testcase�player_first�expected�expected_winnerr   �b�pr	   r	   r
   �test_basic_play_game_1   s    

z$TestTicTacToe.test_basic_play_game_1c             C   s�   t jdddgdddgdddgg�}d}t jdddgdddgdddgg�}d}t||�}|j� \}}| j||� | j|j� |j� � d S )Nr   r   r   r   )r   �arrayr   r   r   r   )r   r   r   r   r   r   r   r   r	   r	   r
   �test_basic_play_game_2   s    
z$TestTicTacToe.test_basic_play_game_2c             C   s�   t jdddgdddgdddgg�}d}t jdddgdddgdddgg�}d}t||�}|j� \}}| j||� | j|j� |j� � d S )Nr   r   r   r   )r   r   r   r   r   r   )r   r   r   r   r   r   r   r   r	   r	   r
   �test_basic_play_game_3-   s    
z$TestTicTacToe.test_basic_play_game_3c             C   s�   dt jdddgdddgdddgg� }d}dt jdddgdddgdddgg� }d}t||�}|j� \}}| j||� | j|j� |j� � d S )	Nr   r   r   r   r   r   r   r   )r   r   r   r   r   r   )r   r   r   r   r   r   r   r   r	   r	   r
   �test_basic_play_game_4>   s    
z$TestTicTacToe.test_basic_play_game_4c             C   s�   dt jdddgdddgdddgg� }d}dt jdddgdddgdddgg� }d}t||�}|j� \}}| j||� | j|j� |j� � d S )	Nr   r   r   r   r   r   r   r   )r   r   r   r   r   r   )r   r   r   r   r   r   r   r   r	   r	   r
   �test_basic_play_game_5O   s    
z$TestTicTacToe.test_basic_play_game_5c             C   s�   dt jdddgdddgdddgg� }d}dt jdddgdddgdddgg� }d}t||�}|j� \}}| j||� | j|j� |j� � d S )	Nr   r   r   r   r   r   r   r   )r   r   r   r   r   r   )r   r   r   r   r   r   r   r   r	   r	   r
   �test_basic_play_game_6`   s    
z$TestTicTacToe.test_basic_play_game_6c       
      C   s�   t jdddgdddgdddgg�}d}t jdddgdddgd	dd
gg�}t jdddgdddgdddgg�}d}t||�}|j� \}}tdj|�� t j||�p�t j||�}	| j||� | j|	� d S )Nr   r   z
final board = 
{}r   r   r   r   r   r   r   r   r   r   r   r   )	r   r   r   r   r   r   Zarray_equalr   Z
assertTrue)
r   r   r   Z
expected_1Z
expected_2r   r   r   r   Zcorrectr	   r	   r
   �test_play_game_1q   s$    
zTestTicTacToe.test_play_game_1N)�__name__�
__module__�__qualname__r   r   r   r   r   r    r!   r"   r	   r	   r	   r
   r      s   r   )Ztictacr   ZunittestZnumpyr   ZTestCaser   �mainr	   r	   r	   r
   �<module>   s
    