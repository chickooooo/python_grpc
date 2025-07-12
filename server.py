import grpc
import time
from concurrent import futures
import order_service_pb2
import order_service_pb2_grpc


class OrderServiceServicer(order_service_pb2_grpc.OrderServiceServicer):
    def PlaceOrder(self, request, context):
        print("Received order request:")
        print(f"  Size: {request.size} inch")
        print(f"  Toppings: {[topping for topping in request.toppings]}")
        print(f"  Customer ID: {request.customer_id}")

        # Simulate order placement logic
        order_id = "ORD123456"
        status = 0  # assuming 0 means success

        return order_service_pb2.OrderResponse(status=status, order_id=order_id)

    def StreamOrderStatus(self, request, context):
        print(f"Streaming status updates for Order ID: {request.order_id}")

        # Simulate streaming of order status over time
        statuses = [
            order_service_pb2.OrderStatus_RECEIVED,
            order_service_pb2.OrderStatus_INPROGRESS,
            order_service_pb2.OrderStatus_COMPLETED,
        ]

        for status in statuses:
            response = order_service_pb2.StatusResponse(status=status)
            yield response

            time.sleep(1)  # Simulate delay between status updates


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    order_service_pb2_grpc.add_OrderServiceServicer_to_server(
        OrderServiceServicer(), server
    )

    port = "50051"
    server.add_insecure_port(f"[::]:{port}")
    server.start()

    print(f"Server started on port {port}")
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
