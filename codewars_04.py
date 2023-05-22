# Versions manager
# You have to implement a VersionManager class.
# It should accept an optional parameter that represents the initial version.
# The input will be in one of the following formats: "{MAJOR}", "{MAJOR}.{MINOR}",
#  or "{MAJOR}.{MINOR}.{PATCH}". More values may be provided after PATCH but they
# should be ignored. If these 3 parts are not decimal values, an exception with
# the message "Error occured while parsing version!" should be thrown.
# If the initial version is not provided or is an empty string, use "0.0.1"
# by default.
# This class should support the following methods, all of which should be
# chainable (except release):
# major() - increase MAJOR by 1, set MINOR and PATCH to 0
# minor() - increase MINOR by 1, set PATCH to 0
# patch() - increase PATCH by 1
# rollback() - return the MAJOR, MINOR, and PATCH to their values before the
# previous major/minor/patch call, or throw an exception with the message
# "Cannot rollback!" if there's no version to roll back to.
# Multiple calls to rollback() should be possible and restore the version history
# release() - return a string in the format "{MAJOR}.{MINOR}.{PATCH}"
# https://www.codewars.com/kata/5bc7bb444be9774f100000c3

class VersionManager:
    def __init__(self, version='0.0.1'):
        self._ver_history = []
        if version:
            self._ver = ['0', '0', '0']
            ver_part_num = 0
            for ver_part in version.split('.')[:3]:
                if ver_part.isdecimal():
                    self._ver[ver_part_num] = ver_part
                else:
                    raise ValueError('Error occured while parsing version!')
                ver_part_num += 1
        else:
            self._ver = ['0', '0', '1']

    def release(self):
        return f"{self._ver[0]}.{self._ver[1]}.{self._ver[2]}"

    def major(self):
        self._ver_history.append(self._ver.copy())
        self._ver[0] = int(self._ver[0]) + 1
        self._ver[1] = '0'
        self._ver[2] = '0'
        return self

    def minor(self):
        self._ver_history.append(self._ver.copy())
        self._ver[1] = int(self._ver[1]) + 1
        self._ver[2] = '0'
        return self

    def patch(self):
        self._ver_history.append(self._ver.copy())
        self._ver[2] = int(self._ver[2]) + 1
        return self

    def rollback(self):
        if len(self._ver_history) > 0:
            self._ver = self._ver_history.pop()
            return self
        else:
            raise ValueError('Cannot rollback!')


print(VersionManager().release() == "0.0.1")
print(VersionManager("").release() == "0.0.1")
print(VersionManager("1.2.3").release() == "1.2.3")
print(VersionManager("1.2.3.4").release() == "1.2.3")
print(VersionManager("1.2.3.d").release() == "1.2.3")
print(VersionManager("1").release() == "1.0.0")
print(VersionManager("1.1").release() == "1.1.0")

print(VersionManager().major().release() == "1.0.0")
print(VersionManager("1.2.3").major().release() == "2.0.0")
print(VersionManager("1.2.3").major().major().release() == "3.0.0")
print(VersionManager("10.11.12").major().major().release() == "12.0.0")

print(VersionManager().patch().release() == "0.0.2")
print(VersionManager("1.2.3").patch().release() == "1.2.4")
print(VersionManager("4").patch().patch().release() == "4.0.2")


print(VersionManager().major().rollback().release() == "0.0.1")
print(VersionManager().minor().rollback().release() == "0.0.1")
print(VersionManager().patch().rollback().release() == "0.0.1")
print(VersionManager().major().patch().rollback().release() == "1.0.0")
print(VersionManager().major().patch().rollback().major().rollback().release() == "1.0.0")
print(VersionManager().major().patch().rollback().rollback().release() == "0.0.1")
