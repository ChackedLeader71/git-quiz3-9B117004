import json
from pkg.book_tools import read_books, write_books, search_books, show_books


def main():
    while True:
        try:
            books = read_books('books.json')
            break
        except (FileNotFoundError, json.JSONDecodeError, OSError) as e:
            print(f"讀取資料時出現錯誤: {e}")
            return

    while True:
        print("--- 簡易書籍管理系統 ---")
        print("1. 顯示全部書籍")
        print("2. 新增書籍")
        print("3. 查詢書籍")
        print("4. 變更借閱狀態")
        print("5. 顯示最後 3 筆書籍與統計")
        print("6. 匯出書籍資料")
        print("7. 離開系統")
        print("------------------------")
        choice = input("請選擇功能：")

        if choice == '1':
            show_books(books)
        elif choice == '2':
            add_book(books)
        elif choice == '3':
            search_for_books(books)
        elif choice == '4':
            change_borrow_status(books)
        elif choice == '5':
            display_last_three_books(books)
        elif choice == '6':
            export_books(books)
        elif choice == '7':
            print("系統已退出")
            break
        else:
            print("無效選項，請重新選擇。")


def add_book(books):
    while True:
        book_id = input("請輸入書籍編號：").strip()
        if not book_id:
            print("書籍編號不可為空，請重新輸入。")
            continue
        if any(book["id"] == book_id for book in books):
            print("書籍編號已存在，請重新輸入。")
            continue
        break

    title = input("請輸入書名：").strip()
    author = input("請輸入作者：").strip()
    while True:
        try:
            price = int(input("請輸入價格："))
            if price <= 0:
                print("價格須為大於 0 的整數，請重新輸入。")
                continue
            break
        except ValueError:
            print("價格須為大於 0 的整數，請重新輸入。")

    new_book = {
        "id": book_id,
        "title": title,
        "author": author,
        "price": price,
        "borrowed": False
    }
    books.append(new_book)
    print("新增成功。")


def search_for_books(books):
    keyword = input("請輸入書名關鍵字：").strip()
    if not keyword:
        print("關鍵字不可為空，請重新輸入。")
        return

    results = search_books(books, keyword)
    show_books(results)


def change_borrow_status(books):
    book_id = input("請輸入書籍編號：").strip()
    for book in books:
        if book["id"] == book_id:
            book["borrowed"] = not book["borrowed"]
            status = "已借出" if book["borrowed"] else "可借閱"
            print(f"「{book['title']}」的狀態已變更為：{status}")
            return

    print("查無此書籍編號")


def display_last_three_books(books):
    print("--- 最後 3 筆書籍 ---")
    last_books = books[-3:] if len(books) >= 3 else books
    show_books(last_books)

    total_books = len(books)
    if total_books == 0:
        print("目前沒有書籍資料")
        return

    available_count = sum(1 for book in books if not book["borrowed"])
    borrowed_count = total_books - available_count
    total_price = sum(book["price"] for book in books)
    average_price = total_price / total_books if total_books > 0 else 0

    print("--- 書籍統計 ---")
    print(f"書籍總數：{total_books}")
    print(f"可借閱：{available_count}")
    print(f"已借出：{borrowed_count}")
    print(f"價格合計：{total_price:,} 元")
    print(f"平均價格：{average_price:.2f} 元")


def export_books(books):
    try:
        write_books(books, 'output.json')
        print(f"已匯出 {len(books)} 筆書籍資料至 output.json。")
    except OSError as e:
        print(f"無法寫入檔案: {e}")


if __name__ == '__main__':
    main()
