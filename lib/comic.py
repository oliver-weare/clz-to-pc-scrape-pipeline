import re


class Comic:
    def __init__(self, title, issue, release_year):
        self.title = self.get_clean_title(title)
        self.issue = self.get_clean_issue(issue)
        self.release_year = self.get_clean_release_year(release_year)

    def get_clean_title(self, title):
        lower_title = title.lower()
        split_title = lower_title.split(", vol.")
        just_title = split_title[0]

        replace_cases = [",", ".", " / ", ":", "'", "(dc)"]
        for case in replace_cases:
            if case == " / ":
                just_title = just_title.replace(case, " ")
                continue
            just_title = just_title.replace(case, "")

        return just_title

    def get_clean_issue(self, issue):
        match = re.search(r"\d+", issue)
        if match:
            return match.group(0)

        return None

    def get_clean_release_year(self, release_year):
        match = re.search(r"\b\d{4}\b", release_year)
        if match:
            return match.group(0)

        return None
