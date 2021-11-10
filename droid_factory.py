from typing import Any, Union
from dataclasses import dataclass
from cs_queue import enqueue, dequeue, front, back, empty_queue, make_empty_queue

@dataclass(frozen=False)
class MutableNode:
    value: Any
    next: Union[None, 'MutableNode']

@dataclass(frozen=False)
class Queue:
    size: int
    front: Union[None, MutableNode]
    back: Union[None, MutableNode]

def create_droid(belt):
    serial = 10000
    frame = {'head':False, 'body':False, 'legs':False, 'arms':False, 'serial':serial}
    droid = frame.copy()
    while not empty_queue(belt):
        if not droid[belt.front.value]:
            droid[belt.front.value] = True
            print(f'Adding {belt.front.value} to droid...')
            dequeue(belt)
        else:
            part = dequeue(belt)
            enqueue(belt, part)
            print(f'Part {part} not needed, placed back on belt...')
        if False not in droid.values():
            droid = frame.copy()
            print(f'Droid {serial} completed.')
            serial += 1
    if True in droid.values():
        required_parts = [key for key in droid if droid[key] is False]

        print(f"----\nCONSTRUCTION HALTED\nBelt empty, construction on droid {serial} has been stopped\nParts needed for completion:")
        for part in required_parts:
            print(f"{part}")
    print(f"Work completed. {serial - 10000} droids constructed.")

def main():
    belt = make_empty_queue()
    for line in open(input('Enter parts file: ')): # droid_parts_3.txt # droid_parts_3_incomplete.txt #
        enqueue(belt, line.strip())
    create_droid(belt)

main()