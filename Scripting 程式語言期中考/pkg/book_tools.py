import json


def read_books(file_name: str) -> list:
    "讀取 JSON 書籍資料並回傳。"
    with open(file_name, 'r', encoding='utf-8') as f:
        return json.load(f)


def write_books(books: list, file_name: str) -> None:
    "將書籍資料寫入 JSON 檔案。"
    with open(file_name, 'w', encoding='utf-8') as f:
        json.dump(books, f, ensure_ascii=False, indent=4)


def search_books(books: list, keyword: str) -> list:
    "依書名關鍵字查詢書籍並回傳結果。"
    return [book for book in books if keyword.lower() in book["title"].lower()]


def show_books(books: list) -> None:
    "顯示書籍資料。"
    if not books:
        print("目前沒有書籍資料")
        return

    print(f"{'編號':>5} {'書籍編號':<10} {'書名':<20} {'作者':<10} {'價格':>6} {'狀態'}")
    for index, book in enumerate(books, start=1):
        status = "已借出" if book["borrowed"] else "可借閱"
        print(f"{index:>5} {book['id']:<10} {book['title']:<20} {book['author']:<10}{book['price']:>6} {status}")
