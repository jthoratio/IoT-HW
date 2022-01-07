from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions

import os
import os.path as osp
import sys
BUILD_DIR = osp.join(osp.dirname(osp.abspath(__file__)), "../build/service/")
sys.path.insert(0, BUILD_DIR)
import argparse

import grpc
from concurrent import futures
import fib_pb2
import fib_pb2_grpc
import log_pb2
import log_pb2_grpc

import paho.mqtt.client as mqtt

import json


# Create your views here.        

class FibonacciView(APIView):
    permission_classes = (permissions.AllowAny,)
    

    def post(self, request):
        body = json.loads(request.body.decode('utf-8'))
        order = body['order']
        
        # Establish connection to mqtt
        client = mqtt.Client()
        client.connect(host = '0.0.0.0', port = 1883)
        client.loop_start()
        client.publish(topic = "log", payload = order)
        client.loop_stop()

        # gRPC
        host = f"{'0.0.0.0'}:{'8080'}"
        print(host)
        with grpc.insecure_channel(host) as channel:
            stub = fib_pb2_grpc.FibCalculatorStub(channel)

            request = fib_pb2.FibRequest()
            request.order = order

            response = stub.Compute(request)
            print(response.value)
        return Response(data = {"result": response.value}, status = 200)

            
            
class LogsView(APIView):
    permission_classes = (permissions.AllowAny,)
    
    def get(self, request):
    
        host = f"{'0.0.0.0'}:{'8081'}"
        print(host)
        with grpc.insecure_channel(host) as channel:
            stub = log_pb2_grpc.LogStub(channel)
            request = log_pb2.LogRequest()
            response = stub.History(request)
        
        return Response(data = {"history": response.value[:]}, status = 200)
            
            
            
            
            
            
            
            
            



