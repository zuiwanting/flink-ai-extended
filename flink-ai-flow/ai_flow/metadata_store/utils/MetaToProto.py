#
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
#
from typing import List

from ai_flow.meta.artifact_meta import ArtifactMeta
from ai_flow.meta.example_meta import ExampleMeta
from ai_flow.meta.job_meta import JobMeta
from ai_flow.meta.model_relation_meta import ModelRelationMeta, ModelVersionRelationMeta
from ai_flow.meta.project_meta import ProjectMeta
from ai_flow.meta.workflow_execution_meta import WorkflowExecutionMeta
from ai_flow.rest_endpoint.protobuf.message_pb2 import ExampleProto, ExampleSupportTypeProto, DataTypeProto, \
    SchemaProto, ProjectProto, JobProto, WorkflowExecutionProto, \
    ModelRelationProto, ModelVersionRelationProto, ModelProto, ModelVersionProto, StateProto, ArtifactProto, \
    ModelVersionStage
from ai_flow.rest_endpoint.service import stringValue, int64Value


class MetaToProto:
    @staticmethod
    def example_meta_to_proto(example_mata) -> ExampleProto:
        if example_mata is None:
            return None
        else:
            example_support_type = ExampleSupportTypeProto.Value(example_mata.support_type)
            if example_mata.schema is not None:
                name_list = example_mata.schema.name_list
                type_list = example_mata.schema.type_list
                data_type_list = []
                if type_list is not None:
                    for data_type in type_list:
                        data_type_list.append(DataTypeProto.Value(data_type))
                else:
                    data_type_list = None
            else:
                name_list = None
                data_type_list = None
            schema = SchemaProto(name_list=name_list,
                                 type_list=data_type_list)
        return ExampleProto(
            uuid=example_mata.uuid,
            name=example_mata.name,
            support_type=example_support_type,
            properties=example_mata.properties,
            data_type=stringValue(example_mata.data_type),
            data_format=stringValue(example_mata.data_format),
            description=stringValue(example_mata.description),
            batch_uri=stringValue(example_mata.batch_uri),
            stream_uri=stringValue(example_mata.stream_uri),
            create_time=int64Value(example_mata.create_time),
            update_time=int64Value(example_mata.update_time),
            schema=schema,
            catalog_name=stringValue(example_mata.catalog_name),
            catalog_type=stringValue(example_mata.catalog_type),
            catalog_database=stringValue(example_mata.catalog_database),
            catalog_connection_uri=stringValue(example_mata.catalog_connection_uri),
            catalog_version=stringValue(example_mata.catalog_version),
            catalog_table=stringValue(example_mata.catalog_table))

    @staticmethod
    def example_meta_list_to_proto(examples: List[ExampleMeta]) -> List[ExampleProto]:
        list_example_proto = []
        for example in examples:
            list_example_proto.append(MetaToProto.example_meta_to_proto(example))
        return list_example_proto

    @staticmethod
    def project_meta_to_proto(project_meta: ProjectMeta) -> ProjectProto:
        if project_meta is None:
            return None
        else:
            return ProjectProto(
                uuid=project_meta.uuid,
                name=project_meta.name,
                properties=project_meta.properties,
                uri=stringValue(project_meta.uri),
                user=stringValue(project_meta.user),
                password=stringValue(project_meta.password),
                project_type=stringValue(project_meta.project_type))

    @staticmethod
    def project_meta_list_to_proto(projects: List[ProjectMeta]) -> List[ProjectProto]:
        project_proto_list = []
        for project in projects:
            project_proto_list.append(MetaToProto.project_meta_to_proto(project))
        return project_proto_list

    @staticmethod
    def artifact_meta_to_proto(artifact_meta: ArtifactMeta) -> ArtifactProto:
        if artifact_meta is None:
            return None
        else:
            return ArtifactProto(
                uuid=artifact_meta.uuid,
                name=artifact_meta.name,
                properties=artifact_meta.properties,
                data_format=stringValue(artifact_meta.data_format),
                description=stringValue(artifact_meta.description),
                batch_uri=stringValue(artifact_meta.batch_uri),
                stream_uri=stringValue(artifact_meta.stream_uri),
                create_time=int64Value(artifact_meta.create_time),
                update_time=int64Value(artifact_meta.update_time))

    @staticmethod
    def artifact_meta_list_to_proto(artifacts: List[ArtifactMeta]) -> List[ArtifactProto]:
        artifact_proto_list = []
        for artifact in artifacts:
            artifact_proto_list.append(MetaToProto.artifact_meta_to_proto(artifact))
        return artifact_proto_list

    @staticmethod
    def job_meta_to_proto(job_meta: JobMeta) -> JobProto:
        if job_meta is None:
            return None
        else:
            job_state = StateProto.Value(job_meta.job_state)
            return JobProto(
                uuid=job_meta.uuid,
                name=job_meta.name,
                workflow_execution_id=int64Value(job_meta.workflow_execution_id),
                job_state=job_state,
                properties=job_meta.properties,
                job_id=stringValue(job_meta.job_id),
                start_time=int64Value(job_meta.start_time),
                end_time=int64Value(job_meta.end_time),
                log_uri=stringValue(job_meta.log_uri),
                signature=stringValue(job_meta.signature))

    @staticmethod
    def job_meta_list_to_proto(jobs: List[JobMeta]) -> List[JobProto]:
        job_proto_list = []
        for job in jobs:
            job_proto_list.append(MetaToProto.job_meta_to_proto(job))
        return job_proto_list

    @staticmethod
    def workflow_execution_meta_to_proto(execution_meta: WorkflowExecutionMeta) -> WorkflowExecutionProto:
        if execution_meta is None:
            return None
        else:
            execution_state = StateProto.Value(execution_meta.execution_state)
            return WorkflowExecutionProto(
                uuid=execution_meta.uuid, name=execution_meta.name,
                execution_state=execution_state,
                project_id=int64Value(execution_meta.project_id),
                properties=execution_meta.properties,
                start_time=int64Value(execution_meta.start_time),
                end_time=int64Value(execution_meta.end_time),
                workflow_json=stringValue(execution_meta.workflow_json),
                log_uri=stringValue(execution_meta.log_uri),
                signature=stringValue(execution_meta.signature))

    @staticmethod
    def workflow_execution_meta_list_to_proto(executions: List[WorkflowExecutionMeta]) -> List[WorkflowExecutionProto]:
        execution_proto_list = []
        for execution in executions:
            execution_proto_list.append(MetaToProto.workflow_execution_meta_to_proto(execution))
        return execution_proto_list

    @staticmethod
    def model_relation_meta_to_proto(model_relation_meta: ModelRelationMeta) -> ModelRelationProto:
        if model_relation_meta is None:
            return None
        else:
            return ModelRelationProto(
                uuid=model_relation_meta.uuid,
                name=model_relation_meta.name,
                project_id=int64Value(model_relation_meta.project_id))

    @staticmethod
    def model_relation_meta_list_to_proto(model_relation_meta_list: List[ModelRelationMeta]) -> List[
        ModelRelationProto]:
        model_proto_list = []
        for model in model_relation_meta_list:
            model_proto_list.append(MetaToProto.model_relation_meta_to_proto(model))
        return model_proto_list

    @staticmethod
    def model_version_relation_meta_to_proto(
            model_version_relation: ModelVersionRelationMeta) -> ModelVersionRelationProto:
        if model_version_relation is None:
            return None
        else:
            return ModelVersionRelationProto(
                version=stringValue(model_version_relation.version),
                model_id=int64Value(model_version_relation.model_id),
                workflow_execution_id=int64Value(model_version_relation.workflow_execution_id))

    @staticmethod
    def model_version_relation_meta_list_to_proto(model_version_relation_list: List[ModelVersionRelationMeta]) -> List[
        ModelVersionRelationProto]:
        model_version_list = []
        for model_version in model_version_relation_list:
            model_version_list.append(MetaToProto.model_version_relation_meta_to_proto(model_version))
        return model_version_list

    @staticmethod
    def model_meta_to_proto(model_relation, model_center_detail) -> ModelProto:
        if model_relation is not None and model_center_detail is not None:
            return ModelProto(uuid=model_relation.uuid, name=model_relation.name,
                              project_id=int64Value(model_relation.project_id),
                              model_type=model_center_detail.model_type,
                              model_desc=stringValue(model_center_detail.model_desc))
        else:
            return None

    @staticmethod
    def model_version_meta_to_proto(model_version_relation, model_center_detail) -> ModelVersionProto:
        if model_version_relation is not None and model_center_detail is not None:
            return ModelVersionProto(
                version=stringValue(model_version_relation.version),
                model_id=int64Value(model_version_relation.model_id),
                workflow_execution_id=int64Value(model_version_relation.workflow_execution_id),
                model_path=stringValue(model_center_detail.model_path),
                model_metric=stringValue(model_center_detail.model_metric),
                model_flavor=stringValue(model_center_detail.model_flavor),
                version_desc=stringValue(model_center_detail.version_desc),
                current_stage=model_center_detail.current_stage)
        else:
            return None

    @staticmethod
    def model_version_store_to_proto(model_version_relation, model_center_detail) -> ModelVersionProto:
        if model_version_relation is not None and model_center_detail is not None:
            return ModelVersionProto(
                version=stringValue(model_version_relation.version),
                model_id=int64Value(model_version_relation.model_id),
                workflow_execution_id=int64Value(model_version_relation.workflow_execution_id),
                model_path=stringValue(model_center_detail.model_path),
                model_metric=stringValue(model_center_detail.model_metric),
                model_flavor=stringValue(model_center_detail.model_flavor),
                version_desc=stringValue(model_center_detail.version_desc),
                current_stage=ModelVersionStage.Value(model_center_detail.current_stage.upper()))
        else:
            return None
