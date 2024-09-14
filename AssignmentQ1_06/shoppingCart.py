def addInCart(arr,value):
    arr.append(value)
    return arr

def removeFromCart(arr,value):
    if(value in arr):
        arr.remove(value)
    return arr
        

arrCart = [1,2,3]
#Adding Items
cart = addInCart(arrCart, 4)
print(f"Items in array after inserting new item is {cart} and total items in cart after inserting new item are {len(cart)}")

#removing items
remove = removeFromCart(cart,3)
print(f"Total items in cart after deleting item are {remove} and length is {len(remove)}")



