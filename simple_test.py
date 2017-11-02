import block
import worker

worker = worker.Worker()
worker.set_data("Hello, World!")
worker.set_leading_zeroes(4)
worker.set_previous_block(block.origin_block())

valid_block = worker.find_valid_block()
print(valid_block)
