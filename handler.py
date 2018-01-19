# coding: utf-8
import os, sys
from trello import TrelloClient

def run(event, context): 
  try:
    KEY = os.environ["TRELLO_KEY"]
    SECRET = os.environ["TRELLO_SECRET"]
    ID_BOARD = os.environ["TRELLO_BOARD"]
    ID_LIST_DONE = os.environ["TRELLO_LIST_DONE"]
    ID_LIST_BACKLOG = os.environ["TRELLO_LIST_BACKLOG"]
    IDS_LIST_PROGRESS = os.environ["TRELLO_LISTS_PROGRESS"]
  except Exception as e:
    print 'env variable import error', e
    raise e
  try:
    client = TrelloClient(
      api_key=KEY,
      api_secret=SECRET,
    )
  except Exception as e:
    print e
    raise e
  
  ids_list_progress = IDS_LIST_PROGRESS.split(':')
  board = client.get_board(ID_BOARD)
  for id_list_progress in ids_list_progress:
    list = board.get_list(id_list_progress)
    list.move_all_cards(board.get_list(ID_LIST_BACKLOG))
  board.get_list(ID_LIST_DONE).archive_all_cards()

if __name__ == '__main__':
  run(1, 2)
  

