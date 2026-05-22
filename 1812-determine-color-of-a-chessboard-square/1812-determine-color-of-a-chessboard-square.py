class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        x=coordinates[-1]
        i=int(x)
        if coordinates[0]=='h' or coordinates[0]=='b' or coordinates[0]=='d' or coordinates[0]=='f':
            if i%2!=0:
                return True
            else:
                return False
        else:
            if i%2!=0:
                return False
            else:
                return True