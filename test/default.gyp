# Copyright 2015 the V8 project authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

{
  'conditions': [
    ['test_isolation_mode != "noop"', {
      'targets': [
        {
          'target_name': 'default_run',
          'type': 'none',
          'dependencies': [
            'cctest/cctest.gyp:cctest_run',
            'intl/intl.gyp:intl_run',
            'message/message.gyp:message_run',
            'mjsunit/mjsunit.gyp:mjsunit_run',
            'preparser/preparser.gyp:preparser_run',
          ],
          'includes': [
            '../build/isolate.gypi',
          ],
          'sources': [
            'default.isolate',
          ],
        },
      ],
    }],
  ],
}
