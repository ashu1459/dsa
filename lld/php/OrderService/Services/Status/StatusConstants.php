<?php

namespace Services\Status;

Class StatusConstants {
    public const INIT = 'INIT';
    public const RECEIVED = 'RECEIVED';
    public const DISPATCHED = 'DISPATCHED';
    public const IN_TRANSIT = 'IN_TRANSIT';
    public const OUT_FOR_DELIVERY = 'OUT_FOR_DELIVERY';
    public const DELIVERED = 'DELIVERED';
    public const COMPLETED = 'COMPLETED';
    public const CANCELLED = 'CANCELLED';

    /**
     * @return array List of Statuses
     */
    public static function getAllStatuses() {
        return [
            self::INIT,
            self::RECEIVED,
            self::DISPATCHED,
            self::IN_TRANSIT,
            self::OUT_FOR_DELIVERY,
            self::DELIVERED,
            self::COMPLETED,
            self::CANCELLED
        ];
    }

    /**
     * @param string $status
     * 
     * @return bool
     */
    public static function statusExists($status) {
        return in_array($status, self::getAllStatuses());
    }
}