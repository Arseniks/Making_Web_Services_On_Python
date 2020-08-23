from bs4 import BeautifulSoup
import unittest


def parse(path_to_file):
    with open(path_to_file, encoding='utf8') as f:
        html = f.read()
    soup = BeautifulSoup(html)
    tags = soup(id='bodyContent')[0]

    imgs = 0
    for tag in tags.find_all('img'):
        if 'width' in tag.attrs and int(tag['width']) >= 200:
            imgs += 1

    headers = 0
    for i in tags.find_all(name=['h1', 'h2', 'h3', 'h4', 'h5', 'h6']):
        if i.text[0] in ['E', 'T', 'C']:
            headers += 1

    linkslen = 0
    every = tags.find_all('a')
    linklen = 1
    for i in every:
        next = i.find_next_siblings()
        if len(next) > 0 and str(next[0].name) == 'a':
            linklen += 1
        else:
            linkslen = max(linklen, linkslen)
            linklen = 1
    lists = 0
    for tag in tags.find_all(['ul', 'ol']):
        if len(tag.find_parents(['ul', 'ol'])) == 0:
            lists += 1

    return [imgs, headers, linkslen, lists]


class TestParse(unittest.TestCase):
    def test_parse(self):
        test_cases = (
            ('wiki/Stone_Age', [13, 10, 12, 40]),
            ('wiki/Brain', [19, 5, 25, 11]),
            ('wiki/Artificial_intelligence', [8, 19, 13, 198]),
            ('wiki/Python_(programming_language)', [2, 5, 17, 41]),
            ('wiki/Spectrogram', [1, 2, 4, 7]),)

        for path, expected in test_cases:
            with self.subTest(path=path, expected=expected):
                self.assertEqual(parse(path), expected)


if __name__ == '__main__':
    unittest.main()
