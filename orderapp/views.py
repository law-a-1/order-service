import requests
import pika
from datetime import datetime
from rest_framework.decorators import api_view
from rest_framework.views import Response
from rest_framework import status
from .models import Order

#Kenapa ga pake username? Karena satu orang bisa checkout lebih dari sekali
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
    elif request.method == 'PUT':
        try:
            try:
                token = request.headers['Authorization']
                r = requests.get('https://auth-law-a1.herokuapp.com/user', headers={"Authorization": token}).json()
                if r["role"] == "admin":
                    try:
                        order = Order.objects.get(pk = id)
                        order.order_status = request.data.get("order_status")
                        order.order_date = datetime.now()
                        #TODO: Tembak ke API SAE
                        # cart = requests.get('https://checkoutservive.herokuapp.com/cart', params={"username" : username}).json() 
                        #TODO : Dapetin cart dari sae
                        # order.total = cart["grand_total"]
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

@api_view(['POST'])
def create_order(request):
    try:
        try:
            token = request.headers['Authorization']
            r = requests.get('https://auth-law-a1.herokuapp.com/user', headers={"Authorization": token}).json()
            username = r["username"]
            #TODO: Tembak ke API SAE
            # cart = requests.get('https://checkoutservive.herokuapp.com/cart', params={"username" : username}).json() 
            order = Order.objects.create(
                username=username,
                order_date = datetime.now())
            #TODO : Dapetin cart dari sae
            # order.total = cart["grand_total"]
            order.save()

            #TODO: Bilang sae untuk tambahin order id di cart, default 0
            content = {
                "order_id" : order.id,
                "message" : "Object succesfully created",
            }
            logging = {
                "type": "INFO",
                "service" : "order",
                "message": "200 - Order is created"
            }
            requests.post('http://35.225.170.45:2323/logs', json=logging)
            return Response(content, status = status.HTTP_200_OK)
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

@api_view(['POST'])
def notify_status(request,id):
    try:
        try:
            token = request.headers['Authorization']
            r = requests.get('https://auth-law-a1.herokuapp.com/user', headers={"Authorization": token}).json()
            username = r["username"]
            #TODO : Bilang ke sae untuk tambahin field cart_status
            # Nanti abis itu tinggal send
            order = order.objects.get(pk = id)
            order_status = order.order_status
            message = {
                "order_status" : order_status,
            }
            #TODO : Send order status ke checkout service
            connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
            channel = connection.channel()
            channel.queue_declare(queue='notify')
            channel.basic_publish(exchange='', routing_key='notify', body=message)
            #requests.put('https://checkoutservive.herokuapp.com/cart/'+username, data = message)
            content = {
                "message" : "Order status sucessfully notified",
            }
            logging = {
                "type": "INFO",
                "service" : "order",
                "message": "200 - User is notified"
            }
            requests.post('http://35.225.170.45:2323/logs', json=logging)
            connection.close()
            return Response(content, status = status.HTTP_200_OK)
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

@api_view(['POST'])
def send_status(request,id):
    try:
        try:
            token = request.headers['Authorization']
            r = requests.get('https://auth-law-a1.herokuapp.com/user', headers={"Authorization": token}).json()
            username = r["username"]
            if r["role"] == "admin":
                #TODO : Bilang ke sae untuk tambahin field cart_status
                # Nanti abis itu tinggal send
                order = order.objects.get(pk = id)
                order_status = order.order_status
                message = {
                    "order_status" : order_status,
                }
                #TODO : Send order status ke checkout service
                connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
                channel = connection.channel()
                channel.queue_declare(queue='send-status')
                channel.basic_publish(exchange='', routing_key='send-status', body=message)
                #requests.put('https://checkoutservive.herokuapp.com/cart/'+username, data = order_status)
                content = {
                    "message" : "Order status sucessfully sent",
                }
                connection.close()
                return Response(content, status = status.HTTP_200_OK)
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