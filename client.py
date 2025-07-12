import grpc
import order_service_pb2
from order_service_pb2_grpc import OrderServiceStub


def place_order(stub: OrderServiceStub) -> str:
    # Create a request
    request = order_service_pb2.OrderRequest(
        size=12,
        toppings=[
            order_service_pb2.TOPPING_PEPPORONI,
            order_service_pb2.TOPPING_JALAPENO,
        ],
        customer_id="cust_001",
    )

    try:
        response = stub.PlaceOrder(request)
        print("Order placed successfully!")
        print(f"Status: {response.status}")
        print(f"Order ID: {response.order_id}")
        return response.order_id
    except grpc.RpcError as e:
        print(f"gRPC failed while placing order: {e.code()} - {e.details()}")
        return None


def stream_order_status(stub: OrderServiceStub, order_id: str):
    print("\nStreaming order status updates:")
    status_request = order_service_pb2.StatusRequest(order_id=order_id)

    try:
        for status_response in stub.StreamOrderStatus(status_request):
            status_name = order_service_pb2.OrderStatus.Name(status_response.status)
            print(f"Order status: {status_name}")
    except grpc.RpcError as e:
        print(f"gRPC failed while streaming status: {e.code()} - {e.details()}")
        print(e)


def main():
    # Connect to the gRPC server
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = OrderServiceStub(channel)

        # Place the order
        order_id = place_order(stub)
        # Stream the status
        stream_order_status(stub, order_id)


if __name__ == "__main__":
    main()
