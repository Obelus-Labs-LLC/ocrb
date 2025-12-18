from OCRB.measure.events import EventLog, EventType, FailureClass
from OCRB.metrics.ori import compute_ori

def test_ori_computation():
    log = EventLog(run_id="t", workload_id="W1-A")
    log.emit(EventType.RUN_START)
    log.emit(EventType.FAILURE, failure_id="f1", failure_class=FailureClass.AUTONOMOUSLY_RECOVERED)
    log.emit(EventType.RUN_END)

    ori = compute_ori(
        gds=1.0,
        arr=1.0,
        ist=1.0,
        rec=1.0,
        cfr=1.0,
    )

    assert ori.ori == 1.0
