from utils.dicts import get_val, get_val_v2


def test_get_val():
    assert get_val({"vcs": "mercurial"}, "vcs") == "mercurial"
    assert get_val({"vcs": "mercurial"}, "vcs", "git") == "mercurial"
    assert get_val({}, "vcs", "git") == "git"
    assert get_val({}, "vcs", "bazaar") == "bazaar"


def test_get_val_v2():
    assert get_val_v2({"vcs": "mercurial"}, "vcs") == "mercurial"
    assert get_val_v2({"vcs": "mercurial"}, "vcs", "git") == "mercurial"
    assert get_val_v2({}, "vcs", "git") == "git"
    assert get_val_v2({}, "vcs", "bazaar") == "bazaar"


# Можно дополнительно формировать отчет в формате html:
# https://pytest-cov.readthedocs.io/en/latest/reporting.html

# pytest
#         --cov-report html
#         --cov-report xml
#         --cov-report lcov
#         --cov-report annotate
#         --cov=myproj tests/