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


from neutronclient.neutron import v2_0 as neutronV20


class ListIpAvailability(neutronV20.ListCommand):
    """List ip usage of networks"""

    resource = 'network_ip_availability'
    resource_plural = 'network_ip_availabilities'
    list_columns = ['id', 'name', 'total_ips', 'used_ips']
    paginations_support = True
    sorting_support = True
