import json
from boto3.dynamodb.types import TypeDeserializer, TypeSerializer


class FilterModule(object):
    def filters(self):
        return {
            'ansible_to_dynamo':self.ansible_to_dynamo,
            'dynamo_to_ansible':self.dynamo_to_ansible
        }

    def ansible_to_dynamo(self,a):
        serializer = TypeSerializer()
        return {
            k: serializer.serialize(v)
            for k, v in a.items()
        }


    def dynamo_to_ansible(self,a):
        deserializer = TypeDeserializer()
        out = {
            k: deserializer.deserialize(v) 
            for k, v in a.items()
        }  
        return(out)

