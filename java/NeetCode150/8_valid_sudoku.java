class Solution {
    public boolean isValidSudoku(char[][] board) 
    {
        for(int i=0; i<9; i++)
        {
            List<Character> row = new ArrayList<>();
            List<Character> column = new ArrayList<>();
            List<Character> box = new ArrayList<>();
            for(int j=0; j<9; j++)
            {
                if(board[i][j] != '.')
                {
                    for(int k=0; k<row.size(); k++)
                    {
                        if(row.get(k) == board[i][j])
                        {
                            return false;
                        }
                    }
                    row.add(board[i][j]);
                }
                if(board[j][i] != '.')
                {
                    for(int k=0; k<column.size(); k++)
                    {
                        if(column.get(k) == board[j][i])
                        {
                            return false;
                        }
                    }
                    column.add(board[j][i]);
                }
                int box_r = 3 * (i / 3) + (j / 3);
                int box_c = 3 * (i % 3) + (j % 3);
                if(board[box_r][box_c] != '.')
                {
                    for(int k=0; k<box.size(); k++)
                    {
                        if(box.get(k) == board[box_r][box_c])
                        {
                            return false;
                        }
                    }
                    box.add(board[box_r][box_c]);
                }
            }
        }
        return true;    
    }
}
