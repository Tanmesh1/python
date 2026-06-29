###input
# {

# "user": {

# "name": "Amit",

# "address": {

# "city": "Pune",

# "pin": 411001

#         }

#     },

# "role": "Admin"

# }
 

# output
# {
# 'user.name': 'Amit',
# 'user.address.city': 'Pune',
# 'user.address.pin': 411001,
# 'role': 'Admin'
# }

def json_format(a):
    new_d = dict()
    for i in a.keys():
        new_d[i] = a[i]
    print(new_d)
    


a = {

"user": {

"name": "Amit",

"address": {

"city": "Pune",

"pin": 411001

        }

    },

"role": "Admin"

}

# print(a["user"])
json_format(a)
# print(json_format(a))


 