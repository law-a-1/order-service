import requests
from rest_framework.decorators import api_view
from rest_framework.views import Response
from rest_framework import status
from .models import Order

#TODO : Intergrate front-end back-end
@api_view(['GET','PUT'])
def order_service(request, id):
    if request.method == 'GET':
        try:
            try:
                token = request.headers['Authorization']
                r = requests.get('https://auth-law-a1.herokuapp.com/user', headers={"Authorization": token}).json()
                if r["role"] == "admin":
                    try:
                        order = Order.objects.get(pk = id)
                        content = {
                            "order_id": order.id, 
                            "order_status": order.order_status,
                            "order_date": order.order_date,
                            "order_total" : order.order_total 
                        }
                        logging = {
                            "type": "INFO",
                            "service" : "order",
                            "message": "200 - Order is retrieved"
                        }
                        requests.post('http://35.225.170.45:2323/logs', json=logging)

                        return Response(content, status= status.HTTP_200_OK)
                    except:
                        logging = {
                            "type": "ERROR",
                            "service" : "order",
                            "message": "404 - Order not found"
                        }
                        requests.post('http://35.225.170.45:2323/logs', json=logging)

                        return Response({
                            "error": "NOT FOUND",
                            "error_message": "The item you're looking for does not exist."
                        }, status=status.HTTP_404_NOT_FOUND)
                elif r["role"] == "user":
                    username = r["username"]
                    try:
                        order = Order.objects.get(username = username)
                        content = {
                            "order_id": order.id, 
                            "order_status": order.order_status,
                            "order_date": order.order_date,
                            "order_total" : order.order_total 
                        }
                        logging = {
                            "type": "INFO",
                            "service" : "order",
                            "message": "200 - Order is retrieved"
                        }
                        requests.post('http://35.225.170.45:2323/logs', json=logging)

                        return Response(content, status= status.HTTP_200_OK)
                    except:
                        logging = {
                            "type": "ERROR",
                            "service" : "order",
                            "message": "404 - Order not found"
                        }
                        requests.post('http://35.225.170.45:2323/logs', json=logging)

                        return Response({
                            "error": "NOT FOUND",
                            "error_message": "The item you're looking for does not exist."
                        }, status=status.HTTP_404_NOT_FOUND)
                else:
                    logging = {
                        "type": "ERROR",
                        "service" : "order",
                        "message": "401 - User is unauthorized"
                    }
                    requests.post('http://35.225.170.45:2323/logs', json=logging)
                    return Response({
                        "error": "UNAUTHORIZED",
                        "error_message": "You are not allowed to do this operation"
                    }, status=status.HTTP_401_UNAUTHORIZED)
            except:
                logging = {
                    "type": "ERROR",
                    "service" : "order",
                    "message": "401 - User is unauthorized"
                }
                requests.post('http://35.225.170.45:2323/logs', json=logging)
                return Response({
                    "error": "UNAUTHORIZED",
                    "error_message": "You are not allowed to do this operation"
                }, status=status.HTTP_401_UNAUTHORIZED)
        except Exception as e:
            logging = {
                "type": "ERROR",
                "service" : "order",
                "message": "500 - An Error occured. Error details: "+e
            }
            requests.post('http://35.225.170.45:2323/logs', json=logging)    
            content = {
                "error": "Internal Server Error",
                "error_description": "Internal server error. Contact admin for support."
            }
            return Response(content, status = status.HTTP_500_INTERNAL_SERVER_ERROR)
    elif request.method == 'PUT':
        try:
            try:
                token = request.headers['Authorization']
                r = requests.get('https://auth-law-a1.herokuapp.com/user', headers={"Authorization": token}).json()
                if r["role"] == "admin":
                    try:
                        order = Order.objects.get(pk = id)
                        order.order_status = request.data.get("order_status")
                        order.save()
                        content = {
                            "message" : "Order succesfully updated"
                        }
                        logging = {
                            "type": "INFO",
                            "service" : "order",
                            "message": "200 - Order is updated"
                        }
                        requests.post('http://35.225.170.45:2323/logs', json=logging)

                        return Response(content, status= status.HTTP_200_OK)
                    except:
                        logging = {
                            "type": "ERROR",
                            "service" : "order",
                            "message": "404 - Order not found"
                        }
                        requests.post('http://35.225.170.45:2323/logs', json=logging)

                        return Response({
                            "error": "NOT FOUND",
                            "error_message": "The item you're lookign for does not exist."
                        }, status=status.HTTP_404_NOT_FOUND)
                else:
                    logging = {
                        "type": "ERROR",
                        "service" : "order",
                        "message": "401 - User is unauthorized"
                    }
                    requests.post('http://35.225.170.45:2323/logs', json=logging)
                    return Response({
                        "error": "UNAUTHORIZED",
                        "error_message": "You are not allowed to do this operation"
                    }, status=status.HTTP_401_UNAUTHORIZED)
            except:
                logging = {
                    "type": "ERROR",
                    "service" : "order",
                    "message": "401 - User is unauthorized"
                }
                requests.post('http://35.225.170.45:2323/logs', json=logging)
                return Response({
                    "error": "UNAUTHORIZED",
                    "error_message": "You are not allowed to do this operation"
                }, status=status.HTTP_401_UNAUTHORIZED)
        except Exception as e:
            logging = {
                "type": "ERROR",
                "service" : "order",
                "message": "500 - An Error occured. Error details: "+e
            }
            requests.post('http://35.225.170.45:2323/logs', json=logging)    
            content = {
                "error": "Internal Server Error",
                "error_description": "Internal server error. Contact admin for support."
            }
            return Response(content, status = status.HTTP_500_INTERNAL_SERVER_ERROR)