#Simulated API that provides transactional data

from flask import Flask, Response, stream_with_context
import time
import uuid
import random

APP = Flask(__name__)


@APP.route("/very_large_request/<int:rowcount>", methods = ["GET"])
def get_large_request(rowcount):
    '''returns N row of data'''
    def data_generator():
        '''The generator of mock data'''
        '''Simulating Transactions'''
        for i in range(rowcount):
            time.sleep(.1)
            txid = uuid.uuid4()
            uid = uuid.uuid4()
            #creat random data
            amount = round(random.uniform(-10000,10000),2)
            yield f"('{txid}', '{uid}', {amount})\n"
    return Response(stream_with_context(data_generator()))

if __name__ == "__main__":
    APP.run(debug=True)
