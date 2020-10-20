# NOTE: Generated By HttpRunner v3.1.4
# FROM: TestCase/APICase\人事系统_H5\候选人招聘模块\候选人教育背景保存\10.yaml


from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase


class TestCaseT10(HttpRunner):

    config = (
        Config("候选人教育背景保存 - 正常返回")
        .variables(**{"baseUrlH5": "/ehr-entrant"})
        .base_url("$base_url")
    )

    teststeps = [
        Step(
            RunRequest("/$baseUrlH5/entrant/recruit/saveEntrantEduction")
            .post("/$baseUrlH5/entrant/recruit/saveEntrantEduction")
            .with_headers(
                **{"Authorization": "$token_h5", "Content-Type": "application/json"}
            )
            .with_json(
                {
                    "beginDate": "2020-04-01",
                    "certificateName": "测试证书",
                    "certificatePhotoUrl": [
                        {
                            "content": "",
                            "file": {
                                "content": "blob:http://ehr-h5-test.pin-dao.cn/946f8691-7f2b-45f1-b20a-e9b5b4891eed",
                                "dir": "test-pd/tfnh1imr2r80-byz.png",
                            },
                            "message": "",
                            "status": "",
                            "uri": "test-pd/tfnh1imr2r80-byz.png",
                        }
                    ],
                    "endDate": "2020-08-01",
                    "entrantId": "$entrantId",
                    "id": "",
                    "major": "测试专业",
                    "schoolName": "测试",
                    "topDegree": 6,
                }
            )
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal("body.code", 0)
        ),
    ]


if __name__ == "__main__":
    TestCaseT10().test_start()
