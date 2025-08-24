# Split the text 

text = "We are learning pyhon for DevOps"
print(text)
new_text = text.split( )
# print("The new text", new_text)

print(text.split( )[0:3])

arn = "arn:partition:service:region:account-id:resource-type/resource-id"
new_arn = arn.split("/")
print("The new arn is as follow: ",new_arn)
print(arn.split("/")[0])