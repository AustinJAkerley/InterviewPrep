class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) 
    {
        for(int i = 0;i < 9; i++)
        {
            vector<int> row = {};
            vector<int> column = {};
            vector<int> box = {};
            for(int j = 0; j < 9; j++)
            {
                if(board[i][j] != '.')
                {
                    for(int k = 0; k < row.size(); k++)
                    {
                        if(row[k] == board[i][j])
                        {
                            return false;
                        }
                    }
                    row.push_back(board[i][j]);
                }
                if(board[j][i] != '.')
                {
                    for(int k = 0; k < column.size(); k++)
                    {
                        if(column[k] == board[j][i])
                        {
                            return false;
                        }
                    }
                    column.push_back(board[j][i]);
                }
                int box_r = 3 * (i / 3) + (j / 3);
                int box_c = 3 * (i % 3) + (j % 3);
                if(board[box_r][box_c] != '.')
                {
                    for(int k = 0; k < box.size(); k++)
                    {
                        if(box[k] == board[box_r][box_c])
                        {
                            return false;
                        }
                    }
                    box.push_back(board[box_r][box_c]);
                }
            }
        }
        return true;
    }
};
