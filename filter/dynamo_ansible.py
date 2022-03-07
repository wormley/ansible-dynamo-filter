import json
from boto3.dynamodb.types import TypeDeserializer, TypeSerializer


from jinja2.filters import environmentfilter, do_groupby as _do_groupby

from ansible.errors import AnsibleError, AnsibleFilterError, AnsibleFilterTypeError
from ansible.module_utils.six.moves import shlex_quote
from ansible.module_utils.six import string_types, integer_types, reraise
from ansible.module_utils._text import to_bytes, to_native, to_text
from ansible.module_utils.common.collections import is_sequence
from ansible.module_utils.common._collections_compat import Mapping
from ansible.parsing.ajson import AnsibleJSONEncoder

class FilterModule(object):
    def filters(self):
        return {
            'ansible_to_dynamo':self.ansible_to_dynamo,
            'dynamo_to_ansible':self.dynamo_to_ansible
        }

    def ansible_to_dynamo(self,a):
        serializer = TypeSerializer()
        return ({
            k: serializer.serialize(v)
            for k, v in a.items()
        },*args, **kw)



    def dynamo_to_ansible(self,a)

        deserializer = TypeDeserializer()
        out = {
            k: deserializer.deserialize(v) 
            for k, v in json.loads(a).items()
        }  
        return(out, *args, **kw))

