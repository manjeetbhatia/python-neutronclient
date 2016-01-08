# All Rights Reserved
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.
#


from neutronclient.neutron import v2_0 as cmd_base
from neutronclient.neutron import v2_0 as neutronV20


class ListIpNetworkUsage(cmd_base.ListCommand):
    """ List ip usage of networks """
    
    resource = 'network_ip_usage'
    resource_plural = '%ss' % resource
    object_path = '%s' % resource_plural
    resource_path = '/%s/%%s' % resource_plural
    list_columns = ['id', 'name', 'total_ips', 'used_ips',
                    'subnet_ip_allocations', 'ip_version', 'network_id',
                    'network_name']
    paginations_support = True
    sorting_support = True

class ShowIpUsage(neutronV20.ShowCommand):
    """Show information of network usage for a given subnet."""

    resource = 'network_ip_usage'
