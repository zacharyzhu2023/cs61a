.read fa19data.sql

CREATE TABLE obedience AS
  select seven, instructor from students;

CREATE TABLE smallest_int AS
  select time, smallest from students
    where smallest > 2 order by smallest limit 20;

create table matchmaker as
  select student1.pet, student1.song, student1.color, student2.color
    from students as student1, students as student2
      where student1.pet = student2.pet and student1.song = student2.song and student1.time < student2.time;
