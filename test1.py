import random

# 生徒データを作成
students = []
for i in range(1, 21):
    student = {
        "name": f"生徒{i}",
        "国語": random.randint(40, 100),
        "英語": random.randint(40, 100),
        "情報": random.randint(40, 100)
    }
    students.append(student)

# 合計点を計算して追加
for student in students:
    student["合計"] = student["国語"] + student["英語"] + student["情報"]

# 合計点の降順で並び替え
students_sorted = sorted(students, key=lambda x: x["合計"], reverse=True)

# 結果を表示
for student in students_sorted:
    print(f"{student['name']} 国語:{student['国語']} 英語:{student['英語']} 情報:{student['情報']} 合計:{student['合計']}")

# 上位3名を表示
print("\n上位3名:")
for student in students_sorted[:3]:
    print(f"{student['name']} 合計:{student['合計']}")