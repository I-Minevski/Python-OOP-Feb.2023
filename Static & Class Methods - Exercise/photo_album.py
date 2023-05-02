from math import ceil


class PhotoAlbum:
    PHOTOS_PER_PAGE = 4

    def __init__(self, pages: int):
        self.pages = pages
        self.photos = [[] for _ in range(self.pages)]

    @classmethod
    def from_photos_count(cls, photos_count: int):
        return cls(ceil(photos_count / cls.PHOTOS_PER_PAGE))

    def add_photo(self, label):
        for i, page in enumerate(self.photos):
            if len(page) < 4:
                self.photos[i].append(label)
                return f"{label} photo added successfully on page {i+1} slot {len(self.photos[i])}"
        return "No more free slots"

    def display(self):
        lines = []
        result = "-----------\n"
        for page in self.photos:
            line = ' '.join('[]' for x in page)
            lines.append(line)
        result += "\n-----------\n".join(lines)
        result += "\n-----------"
        return result


album = PhotoAlbum(2)
print(album.photos)
print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))

print(album.display())

