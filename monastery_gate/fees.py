"""Fees: a perpetual visit is free; a stay pays accommodation plus GST.

GST slabs follow India's hotel accommodation rates from 22 Sep 2025
(5% up to Rs 7,500 a night, 18% above). Check current rates before charging.
"""
GST_SLABS = [(7500, 0.05), (float("inf"), 0.18)]


def gst_rate(nightly):
    return next(rate for limit, rate in GST_SLABS if nightly <= limit)


def quote(visitor_id, nights=0, nightly=0.0):
    """Quote a visit (nights=0) or a stay. Amounts are in rupees."""
    if nights == 0:
        return {"visitor_id": visitor_id, "kind": "perpetual visit",
                "accommodation": 0.0, "gst_rate": 0.0, "gst": 0.0, "total": 0.0}
    base = nights * nightly
    rate = gst_rate(nightly)
    gst = round(base * rate, 2)
    return {"visitor_id": visitor_id, "kind": "stay", "accommodation": base,
            "gst_rate": rate, "gst": gst, "total": round(base + gst, 2)}
