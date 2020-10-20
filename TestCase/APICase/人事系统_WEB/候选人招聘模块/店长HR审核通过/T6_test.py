# NOTE: Generated By HttpRunner v3.1.4
# FROM: TestCase/APICase\人事系统_WEB\候选人招聘模块\店长HR审核通过\6.yaml


import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent.parent.parent))


from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase

from TestCase/APICase.人事系统_H5.候选人招聘模块.候选人提交信息.T22_test import TestCaseT22 as T22


class TestCaseT6(HttpRunner):

    config = (
        Config("店长HR审核通过 - 正常返回")
        .variables(**{"baseUrl": "ehr-admin"})
        .base_url("$base_url")
    )

    teststeps = [
        Step(RunTestCase("候选人提交信息 - 正常返回").call(T22)),
        Step(
            RunRequest("$baseUrl/entrant/recruit/pageEntrant")
            .post("$baseUrl/entrant/recruit/pageEntrant")
            .with_headers(
                **{"Authorization": "$token", "Content-Type": "application/json"}
            )
            .with_json({"auditStatus": 2, "pageNum": 1, "pageSize": 10})
            .extract()
            .with_jmespath("body.data.list[0].entrantInfoId", "entrantId")
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal("body.code", 0)
        ),
        Step(
            RunRequest("$baseUrl/entrant/recruit/auditPass")
            .post("$baseUrl/entrant/recruit/auditPass")
            .with_headers(
                **{"Authorization": "$token", "Content-Type": "application/json"}
            )
            .with_json({"entrantId": "$entrantId"})
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal("body.code", 0)
        ),
    ]


if __name__ == "__main__":
    TestCaseT6().test_start()
