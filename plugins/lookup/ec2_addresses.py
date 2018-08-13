from __future__ import absolute_import, division, print_function

import boto3
from ansible.plugins.lookup import LookupBase


class LookupModule(LookupBase):

    def run(self, terms, variables=None, **kwargs):
        ret = []
        if not terms:
            terms = [{}]
        for term in terms:
            if 'region' in term:
                ec2 = boto3.client('ec2', region_name=term['region'])
            else:
                ec2 = boto3.client('ec2')
            address = ec2.describe_addresses()
            ret.extend(address['Addresses'])
        return ret

