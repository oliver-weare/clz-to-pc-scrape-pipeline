from .utils import get_match


class Comic:
    def __init__(self, title, issue, release_year):
        self.title = self.get_clean_title(title)
        self.issue = get_match(r"\d+", issue)
        self.release_year = get_match(r"\b\d{4}\b", release_year)

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
