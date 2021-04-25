
import matchers as m

class QueryBuilder:

    def __init__(self, matchers=None, matcher=None):


        if matchers == None:
            matchers = [m.All()]

        self._matchers = matchers

        if matcher:
            self._matchers.append(matcher)


    
    def playsIn(self, team):
        return QueryBuilder(self._matchers, m.PlaysIn(team))
        

    def hasAtLeast(self, value, attr):
        return QueryBuilder(self._matchers, m.HasAtLeast(value, attr))


    def hasFewerThan(self, value, attr):
        return QueryBuilder(self._matchers, m.HasFewerThan(value, attr))
    
   
    def oneOf(self, *matchers):
        return QueryBuilder(None, m.Or(*matchers))

    def build(self):
        match = m.And(*self._matchers)
        self._matchers.clear()
        self._matchers.append(m.All())
        return match

