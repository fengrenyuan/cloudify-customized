########
# Copyright (c) 2014 GigaSpaces Technologies Ltd. All rights reserved
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
#    * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    * See the License for the specific language governing permissions and
#    * limitations under the License.


# 'ctx' is always passed as a keyword argument to operations, so
# your operation implementation must either specify it in the arguments
# list, or accept '**kwargs'. Both are shown here.
import os
from cloudify import ctx

# put the operation decorator on any function that is a task
from cloudify.decorators import operation

# this file is used by cloudify plugin interface implement
# which is defined in plugin.yaml

@operation
def start_hello(**kwargs):
  ctx.logger.info('start workflow')
  target = ctx.node.properties['target']
  ctx.logger.info('hello '+ target)

@operation
def stop_hello(**kwargs):
  ctx.logger.info('stop workflow')
  target = ctx.node.properties['target']
  ctx.logger.info('hello '+ target) 