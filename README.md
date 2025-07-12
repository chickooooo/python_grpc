# Python gRPC Pizza Ordering System 🍕

This is a simple Python-based gRPC example demonstrating a pizza ordering service with both unary and server-streaming RPC calls.

It complements the Medium article: [Python + gRPC walkthrough](https://medium.com/@kshitij2549/python-grpc-walkthrough-fd192009a1c6).

## Overview

This project features a gRPC service where a client can place an order for a pizza and receive status updates on that order.

### Features

- **Unary RPC**: Place a pizza order with size, toppings, and customer ID.
- **Server Streaming RPC**: Stream real-time updates on the status of a pizza order.

## Technologies

- Python 3
- gRPC
- Protocol Buffers

---

## Project Structure

```
.
├── client.py               # Client code to place order and receive status
├── server.py               # gRPC server implementation
├── order_service.proto     # Protocol Buffers service definition
```

---

## Getting Started

### 1. Install Dependencies

```bash
pip install grpcio grpcio-tools
```

### 2. Compile the .proto file

```bash
python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. order_service.proto
```

This will generate:
- `order_service_pb2.py`
- `order_service_pb2_grpc.py`

### 3. Run the gRPC Server

```bash
python server.py
```

### 4. Run the Client

In a separate terminal:

```bash
python client.py
```

---

## Sample Output

```
Order placed successfully!
Status: 0
Order ID: ORD123456

Streaming order status updates:
Order status: OrderStatus_RECEIVED
Order status: OrderStatus_INPROGRESS
Order status: OrderStatus_COMPLETED
```

---

## Protobuf Details

The `.proto` file defines:

- `PlaceOrder`: Unary RPC to place a pizza order.
- `StreamOrderStatus`: Server streaming RPC for order status updates.

Toppings and status use enums for clarity.

---

## License

This project is licensed under the MIT License.

---

Inspired by gRPC learning series. Read the full Medium article: [Python + gRPC walkthrough](https://medium.com/@kshitij2549/python-grpc-walkthrough-fd192009a1c6)
