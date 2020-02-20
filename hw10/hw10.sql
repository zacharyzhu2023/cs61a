CREATE TABLE parents AS
  SELECT "abraham" AS parent, "barack" AS child UNION
  SELECT "abraham"          , "clinton"         UNION
  SELECT "delano"           , "herbert"         UNION
  SELECT "fillmore"         , "abraham"         UNION
  SELECT "fillmore"         , "delano"          UNION
  SELECT "fillmore"         , "grover"          UNION
  SELECT "eisenhower"       , "fillmore";

CREATE TABLE dogs AS
  SELECT "abraham" AS name, "long" AS fur, 26 AS height UNION
  SELECT "barack"         , "short"      , 52           UNION
  SELECT "clinton"        , "long"       , 47           UNION
  SELECT "delano"         , "long"       , 46           UNION
  SELECT "eisenhower"     , "short"      , 35           UNION
  SELECT "fillmore"       , "curly"      , 32           UNION
  SELECT "grover"         , "short"      , 28           UNION
  SELECT "herbert"        , "curly"      , 31;

CREATE TABLE sizes AS
  SELECT "toy" AS size, 24 AS min, 28 AS max UNION
  SELECT "mini"       , 28       , 35        UNION
  SELECT "medium"     , 35       , 45        UNION
  SELECT "standard"   , 45       , 60;

-------------------------------------------------------------
-- PLEASE DO NOT CHANGE ANY SQL STATEMENTS ABOVE THIS LINE --
-------------------------------------------------------------

-- The size of each dog
CREATE TABLE size_of_dogs AS
  SELECT d.name, s.size from dogs as d, sizes as s
  where d.height > s.min and d.height <= s.max;


-- All dogs with parents ordered by decreasing height of their parent
CREATE TABLE by_parent_height AS
  Select p.child
  From dogs as d, parents as p
  Where p.parent = d.name
  order by -height;

-- Filling out this helper table is optional
CREATE TABLE siblings AS
  Select p1.child as child1, p2.child as child2
  From parents as p1, parents as p2
  Where p1.parent = p2.parent and p1.child < p2.child;


-- Sentences about siblings that are the same size
CREATE TABLE sentences AS
  Select d1.name || " and " || d2.name || " are " || size || " siblings"
  From siblings, dogs as d1, dogs as d2, sizes
  Where child1 = d1.name and child2 = d2.name
  and d1.height > min and d1.height <= max and d2.height > min and d2.height <= max;



-- Ways to stack 4 dogs to a height of at least 170, ordered by total height
CREATE TABLE stacks_helper(dogs, stack_height, last_height);
  Insert into stacks_helper select name, height, height from dogs;
  Insert into stacks_helper select dogs || ', ' || name, stack_height + height, height from stacks_helper, dogs where height > last_height;
  Insert into stacks_helper select dogs || ', ' || name, stack_height + height, height from stacks_helper, dogs where height > last_height;
  Insert into stacks_helper select dogs || ', ' || name, stack_height + height, height from stacks_helper, dogs where height > last_height and stack_height + height >= 170;

CREATE TABLE stacks AS
  SELECT dogs, stack_height
  From stacks_helper
  Where stack_height >= 170
  Order by stack_height;
