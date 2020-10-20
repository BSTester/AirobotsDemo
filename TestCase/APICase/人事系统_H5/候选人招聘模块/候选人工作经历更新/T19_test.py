# NOTE: Generated By HttpRunner v3.1.4
# FROM: TestCase/APICase\人事系统_H5\候选人招聘模块\候选人工作经历更新\19.yaml


import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent.parent.parent))


from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase

from TestCase/APICase.人事系统_H5.候选人招聘模块.候选人工作经历保存.T18_test import TestCaseT18 as T18


class TestCaseT19(HttpRunner):

    config = (
        Config("候选人工作经历更新 - 正常返回")
        .variables(**{"baseUrlH5": "/ehr-entrant"})
        .base_url("$base_url")
    )

    teststeps = [
        Step(RunTestCase("候选人工作经历保存 - 正常返回").call(T18)),
        Step(
            RunRequest("/$baseUrlH5/entrant/recruit/modifyEntrantWork")
            .post("/$baseUrlH5/entrant/recruit/modifyEntrantWork")
            .with_headers(
                **{"Authorization": "$token_h5", "Content-Type": "application/json"}
            )
            .with_json(
                [
                    {
                        "beginDate": "2020-03-01",
                        "companyName": "测试公司",
                        "endDate": "2020-08-01",
                        "endTime": "2020-07-31T16:00:00.000Z",
                        "entrantId": "$entrantId",
                        "leaveReason": "11",
                        "position": "测试职位",
                        "startTime": "2020-02-29T16:00:00.000Z",
                        "workOrder": 0,
                        "yearSalary": "11",
                    },
                    {
                        "beginDate": "2020-03-01",
                        "companyName": "测试公司1",
                        "endDate": "2020-08-01",
                        "endTime": "2020-07-31T16:00:00.000Z",
                        "entrantId": "$entrantId",
                        "leaveReason": "22",
                        "position": "测试职位2",
                        "startTime": "2020-02-29T16:00:00.000Z",
                        "workOrder": 1,
                        "yearSalary": "22",
                    },
                    {
                        "beginDate": "2020-03-01",
                        "companyName": "测试公司3",
                        "endDate": "2020-08-01",
                        "endTime": "2020-07-31T16:00:00.000Z",
                        "entrantId": "$entrantId",
                        "leaveReason": "33",
                        "position": "测试职位3",
                        "startTime": "2020-02-29T16:00:00.000Z",
                        "workOrder": 2,
                        "yearSalary": "33",
                    },
                ]
            )
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal("body.code", 0)
        ),
    ]


if __name__ == "__main__":
    TestCaseT19().test_start()
