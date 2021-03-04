# NOTE: Generated By HttpRunner v3.1.4
# FROM: TestCases/APICase/api_demo/menu.yml


from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase


class TestCaseMenu(HttpRunner):

    config = (
        Config("获取菜单")
        .variables(**{"base_url": "https://td.dia03.com"})
        .base_url("$base_url")
        .verify(False)
    )

    teststeps = [
        Step(
            RunRequest("/v1/user/permission-menu")
            .get("/v1/user/permission-menu")
            .with_headers(
                **{
                    "accept": "application/json, text/plain, */*",
                    "accept-encoding": "gzip, deflate, br",
                    "accept-language": "zh-CN,zh-TW;q=0.9,zh;q=0.8,en-US;q=0.7,en;q=0.6",
                    "accountid": "null",
                    "authorization": "Bearer $token",
                    "dnt": "1",
                    "referer": "https://td.dia03.com/user/login?redirect=%2F",
                    "sec-fetch-dest": "empty",
                    "sec-fetch-mode": "cors",
                    "sec-fetch-site": "same-origin",
                    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36",
                }
            )
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal("body.status", 0)
        ),
    ]


if __name__ == "__main__":
    TestCaseMenu().test_start()
