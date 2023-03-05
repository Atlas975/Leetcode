SELECT id FROM Weather WHERE temperature > (SELECT temperature FROM Weather WHERE id = id - 1) AND id > 1;
