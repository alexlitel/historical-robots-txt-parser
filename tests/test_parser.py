from historical_robots.parser import RobotTxtParser


def test_request(mock_request):
    test_req = RobotTxtParser("https://a.com").make_request()
    assert "agent" in test_req


def test_check_valid_line():
    txt_parser = RobotTxtParser("")
    assert not txt_parser.check_valid_line("Allow")
    assert txt_parser.check_valid_line("user-agent")
    assert txt_parser.check_valid_line("Disallow")


def test_check_valid_line_with_allow_rule():
    assert RobotTxtParser("", True).check_valid_line("Allow")


def test_parse_lines():
    lines = "\n".join(["User-agent: *", "Disallow: /test", "Allow: Cool"])
    parsed_lines = RobotTxtParser("").parse_lines(lines)
    assert parsed_lines["*"]["/test"] == "Disallow"


def test_parse(mock_request):
    parsed = RobotTxtParser("https://www.test.com/robots.txt").parse()
    assert parsed["*"]["/test"] == "Disallow"
