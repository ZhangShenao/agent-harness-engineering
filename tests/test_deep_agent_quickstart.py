import unittest

from quickstart.deep_agent_quickstart import extract_final_result_text


class FakeMessage:
    def __init__(self, content: str) -> None:
        self.content = content


class ExtractFinalResultTextTest(unittest.TestCase):
    def test_returns_last_message_content(self) -> None:
        result = {
            "messages": [
                {"role": "user", "content": "北京的天气怎么样？"},
                FakeMessage("北京当前天气：晴。"),
            ]
        }

        self.assertEqual(extract_final_result_text(result), "北京当前天气：晴。")


if __name__ == "__main__":
    unittest.main()
